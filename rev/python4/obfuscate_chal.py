import argparse
import ast
from zlib import compress
from base64 import b85encode
from pathlib import Path
from random import getrandbits, sample

FLAG = "texsaw{python_4_will_never_exist_but_if_it_did_it_might_look_like_this_maybe_but_no_one_can_be_for_sure_did_yall_use_chatgpt_for_this?_let_me_know_if_so}"
ENCODED_FLAG = b85encode(compress(FLAG.encode())).decode()

STRING_MASK_OFFSET = 27
names_mask = dict()


def get_name_mask(name: str) -> str:
    if name not in names_mask:
        while (name_hash := "".join(["_" if getrandbits(1) else "z" for _ in range(1000)])) in names_mask:
            pass
        names_mask.update({name: name_hash})
    return names_mask[name]


def obfuscate_str(s: str) -> str:
    encoded = s
    obfuscated = " ".join(["_" * (ord(c) + STRING_MASK_OFFSET) for c in encoded])
    return obfuscated


def deobfuscate_str(s: str) -> str:
    chars = ""
    for word in s.split(" "):
        chars += chr(len(word) - STRING_MASK_OFFSET)
    return chars


def create_obfuscated_string(text: str) -> str:
    return f"''.join(chr(len(c) - {STRING_MASK_OFFSET}) for c in '{obfuscate_str(text)}'.split(' '))"


def string_to_calls(plaintext: str):
    func_template = """
    def {name}(s=""):
        return s+{c}
    """.strip()

    # get initial flag value
    init_char = plaintext[:1]

    # store ordered function names
    ordered_func_names = []

    # create random function names
    for char in plaintext[1:]:
        while (fname := "".join(["a" if getrandbits(1) else "b" for _ in range(1000)])) in ordered_func_names:
            pass
        ordered_func_names.append(fname)

    # create call chain and and function defs
    flag_calls = create_obfuscated_string(init_char)
    ordered_func_defs = []
    for func_name, char in zip(ordered_func_names, plaintext[1:]):
        flag_calls = func_name + "(" + flag_calls + ")"
        ordered_func_defs.append(func_template.format(name=func_name, c=create_obfuscated_string(char)))

    # randomize order of function defs
    random_function_defs = "\n".join(sample(ordered_func_defs, k=len(ordered_func_defs)))

    return (random_function_defs, flag_calls)


def create_cipher_ast(text: str):
    return ast.parse(create_obfuscated_string(text)).body[0].value


def create_attr_access(base: str, attrname: str):
    inline_get_attr = f"getattr({base}, {ast.unparse(create_cipher_ast(attrname))})"
    return ast.parse(inline_get_attr).body[0].value


class ObfTree(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        node.name = get_name_mask(node.name)
        return node

    def visit_Name(self, node):
        if node.id in dir(__builtins__):
            new_node = create_attr_access("__builtins__", node.id)
            ast.copy_location(new_node, node)
            ast.fix_missing_locations(new_node)
            return new_node
        elif node.id != "REPLACE_ME_WITH_FLAG":
            node.id = get_name_mask(node.id)
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            new_node = create_cipher_ast(node.value)
            ast.copy_location(new_node, node)
            ast.fix_missing_locations(new_node)
            return new_node
        else:
            return node

    def visit_Attribute(self, node):
        self.generic_visit(node)
        new_node = create_attr_access(ast.unparse(node.value), node.attr)
        ast.copy_location(new_node, node)
        ast.fix_missing_locations(new_node)
        return new_node


def create_chal(file: Path, flag: str) -> str:
    source = ast.parse(file.read_text())
    # obfuscate source
    transformed_source = ast.unparse(ast.fix_missing_locations(ObfTree().visit(source)))

    # get obfuscated_flag
    function_defs, obfuscated_flag = string_to_calls(flag)
    # replace flag
    transformed_source = transformed_source.replace("REPLACE_ME_WITH_FLAG", obfuscated_flag)

    return function_defs + "\n" + transformed_source


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="create_chal_src", description="do not provide args to print the flag")
    parser.add_argument("chal", type=Path, nargs="?")
    args = parser.parse_args()
    if args.chal:
        print(create_chal(args.chal, ENCODED_FLAG))
    else:
        print(f"flag        : {FLAG}")
        print(f"encoded flag: {ENCODED_FLAG}")
