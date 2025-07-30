/* jshint esversion: 6 */

if (rights_name_json.includes("file") || window.confirm("应用想要获取 文件读写 权限")) {
    if (!rights_name_json.includes("file")) {
        rights_name_json.push("file");
    }
    localStorage.setItem(ProjectName+"/rights", JSON.stringify(rights_name_json));
    class FileSystem {
        static read(name="") {
            return localStorage.getItem(ProjectName + name);
        }

        static write(name="", value="") {
            let File_name_json = JSON.parse(localStorage.getItem(ProjectName+"/files")) || [];
            File_name_json.push(ProjectName + name);
            localStorage.setItem(ProjectName+"/files", JSON.stringify(File_name_json));
            localStorage.setItem(ProjectName + name, value);
            return value;
        }

        static delete(name="") {
            let File_name_json = JSON.parse(localStorage.getItem(ProjectName+"/files")) || [];
            File_name_json = File_name_json.filter(item => item !== (ProjectName + name));
            localStorage.setItem(ProjectName+"/files", JSON.stringify(File_name_json));
            localStorage.removeItem(ProjectName + name);
        }
    }
    window.FileSystem = FileSystem
}