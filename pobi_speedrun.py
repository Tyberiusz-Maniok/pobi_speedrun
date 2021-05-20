import sys

dir_path = str(sys.argv[1])
if dir_path[-1] != "/":
    dir_path += "/"
call_params = sys.argv[2:]

TYPE_DICT = {
    "int" : "int",
    "uint" : "unsigned int",
    "string" : "std::string",
    "float" : "float",
    "double" : "double",
    "bool" : "bool",
    "char" : "char"
}

def capitalize_name(name):
    name_c = name.split("_")
    for i in range(len(name_c)):
        name_c[i] = name_c[i].capitalize()
    return "".join(name_c)

def write_cpp(name, params):
    name_c = capitalize_name(name)
    with open(dir_path + "src/" + name + ".cpp", "w") as f_cpp:
        f_cpp.write('#include "' + name + '.h"\n\n')
        f_cpp.write(name_c + "::" + name_c + "(")
        constructor_params = []
        init_list = []
        for param in params:
            p = param.split(":")
            constructor_params.append(TYPE_DICT[p[1]] + " " + p[0])
            init_list.append(p[0] + "(" + p[0] + ")")
        f_cpp.write(", ".join(constructor_params))
        f_cpp.write(") :\n")
        f_cpp.write(", ".join(init_list))
        f_cpp.write("{}\n\n" + name_c + "::~" + name_c + "(){}\n\n")
        for param in params:
            p = param.split(":")
            type_get = "is" if TYPE_DICT[p[1]] == "bool" else "get"
            f_cpp.write("const " + TYPE_DICT[p[1]] + " " + name_c + "::" + type_get + p[0].capitalize() + "() const\n{\n\treturn this->" + p[0] + ";\n}\n\n")

def write_h(name, params):
    name_c = capitalize_name(name)
    with open(dir_path + "include/" + name + ".h", "w") as f_h:
        f_h.write("#ifndef " + name.upper() + "_H\n#define " + name.upper() + "_H\n\n")
        f_h.write("class " + name_c +"\n{\n\tprivate:\n")
        constructor_params = []
        for param in params:
            p = param.split(":")
            constructor_params.append(TYPE_DICT[p[1]])
            f_h.write("\t\t" + TYPE_DICT[p[1]] + " " + p[0] + ";\n")
        f_h.write("\n\tpublic:\n\t\t" + name_c + "(")
        f_h.write(", ".join(constructor_params) + ");\n\t\t~" + name_c + "();\n")
        for param in params:
            p = param.split(":")
            type_get = "is" if TYPE_DICT[p[1]] == "bool" else "get"
            f_h.write("\t\tconst " + TYPE_DICT[p[1]] + " " + type_get + p[0].capitalize() + "() const;\n")
        f_h.write("\n};\n#endif")
            
def write_files(s):
    cls_name = s[0]
    write_h(cls_name, s[1:])
    write_cpp(cls_name, s[1:])

write_files(list(map(lambda x : str(x), call_params)))
