
import textwrap, sys

All_modules= ", ". join(sorted(sys . builtin_module_names))

print(textwrap.fill(All_modules, width = 200))


print(help("modules"))