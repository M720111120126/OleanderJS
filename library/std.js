/* jshint esversion: 8 */

let denied = false;
let notification = null;
class push {
    async askForNotificationPermission() {
        try {
            const allowedByBrowser = await Notification.requestPermission();
            if (!allowedByBrowser) {
                throw new Error('Denied by browser');
            }
            denied = false;
            return true;
        } catch (e) {
            denied = true;
            console.warn('Could not request notification permissions', e);
            return false;
        }
    }
    requestPermission() {
        return this.askForNotificationPermission();
    }

    hasPermission() {
        if (denied) {
            return false;
        }
        return this.askForNotificationPermission();
    }

    async _showNotification(text) {
        if (await this.hasPermission()) {
            notification = new Notification('Notification from project', {
                body: text
            });
        }
    }

    showNotification(text) {
        this._showNotification(text);
    }

    closeNotification() {
        if (notification) {
            notification.close();
        }
    }
}