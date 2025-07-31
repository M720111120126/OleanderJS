from dependencies.ObjectArkOfPython import CompilationLow
import sys, os

if len(sys.argv) < 2:
    print("Usage: OJC.py <input_file.yh>")
    sys.exit(1)
with open(sys.argv[1], "r", encoding="utf-8") as f_r:
    with open(os.path.basename(sys.argv[1]).replace(".yh", ".html"), "w", encoding="utf-8") as f_w:
        f_w.write(CompilationLow(f_r.read(), os.path.basename(sys.argv[1])))
