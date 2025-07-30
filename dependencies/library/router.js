/* jshint esversion: 6 */

class router {
    static pushUrl(url) {
        window.location.assign(url);
    }

    static back(url="") {
        if (url === "") {
            window.history.back();
        } else {
            window.location.replace(url);
        }
    }
}