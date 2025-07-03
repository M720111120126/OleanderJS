/* jshint esversion: 6 */

if (rights_name_json.includes("OSfile") || window.confirm("应用想要获取 完全访问文件 权限")) {
    rights_name_json.push("OSfile");
    localStorage.setItem("Oleander/rights", JSON.stringify(rights_name_json));
    class OleanderFileSystem {
        static read(name="") {
            return localStorage.getItem("Oleander" + name);
        }

        static write(name="", value="") {
            let File_name_json = JSON.parse(localStorage.getItem("Oleander"+"/files")) || [];
            File_name_json.push("Oleander" + name);
            localStorage.setItem("Oleander/files", JSON.stringify(File_name_json));
            localStorage.setItem("Oleander" + name, value);
            return value;
        }

        static delete(name="") {
            let File_name_json = JSON.parse(localStorage.getItem("Oleander"+"/files")) || [];
            File_name_json = File_name_json.filter(item => item !== ("Oleander" + name));
            localStorage.setItem("Oleander/files", JSON.stringify(File_name_json));
            localStorage.removeItem("Oleander" + name);
        }
    }
    window.FileSystem = FileSystem
}