/* jshint esversion: 6 */

class KVManager {
    static init() {
        this.KVStorename = "";
    }

    static getKVStore(KVStorename="test", encrypt=false, key="") {
        this.KVStorename = KVStorename;
        this.encrypt = encrypt;
        this.key = key;
    }

    static get(key="") {
        if (this.encrypt) {
            return blockCipher.decryptString(this.key, JSON.parse(localStorage.getItem(this.KVStorename + key)));
        } else {
            return localStorage.getItem(this.KVStorename + key);
        }
    }

    static put(key="", value="") {
        let Data_name_json = JSON.parse(localStorage.getItem(this.KVStorename)) || [];
        Data_name_json.push(this.KVStorename + key);
        localStorage.setItem(this.KVStorename, JSON.stringify(Data_name_json));
        if (this.encrypt) {
            localStorage.setItem(this.KVStorename + key, JSON.stringify(blockCipher.encryptString(this.key, value)));
        } else {
            localStorage.setItem(this.KVStorename + key, value);
        }
        return value;
    }

    static delete(key="") {
        let Data_name_json = JSON.parse(localStorage.getItem(this.KVStorename)) || [];
        Data_name_json = Data_name_json.filter(item => item !== (this.KVStorename + key));
        localStorage.setItem(this.KVStorename, JSON.stringify(Data_name_json));
        localStorage.removeItem(this.KVStorename + key);
    }

    static closeKVStore() {
        this.KVStorename = "";
        this.encrypt = "";
    }

    static deleteKVStore() {
        let Data_name_json = JSON.parse(localStorage.getItem(this.KVStorename)) || [];
        for (let Data_name of Data_name_json) {
            localStorage.removeItem(Data_name);
        }
        localStorage.removeItem(this.KVStorename);
        this.KVStorename = "";
        this.encrypt = "";
    }
}