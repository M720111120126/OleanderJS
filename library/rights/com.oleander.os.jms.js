/* jshint esversion: 6 */

if (rights_name_json.includes("jms") || window.confirm("应用想要获取 JZH账号 权限")) {
    if (!rights_name_json.includes("jms")) {
        rights_name_json.push("jms");
    }
    localStorage.setItem(ProjectName+"/rights", JSON.stringify(rights_name_json));
    let jms_window = null;
    let cipher = Date.now().toString();
    class jms{
        static request() {
            jms_window = window.open(`https://jms.xn--jzh-k69dm57c4fd.xyz/jms.php?cipher=${cipher}`, "", "width=200,height=100");
        }
        static state() {
            if (jms_window) {
                if (jms_window.closed) {
                    if (localStorage.getItem(cipher) === "NO") {
                        return -1;
                    }
                    return 2;
                } else {
                    return 1;
                }
            } else {
                return 0;
            }
        }
        static get() {
            let user_json = localStorage.getItem(cipher);
            localStorage.removeItem(cipher);
            return JSON.parse(user_json);
        }
    }
}