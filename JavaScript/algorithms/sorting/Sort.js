export default class Sort {
    constructor(originalCallbacks) {
        this.callbacks = Sort.initSortingCallbacks(originalCallbacks);
    }

    static initSortingCallbacks(originalCallbacks) {
        const callbacks = originalCallbacks || {};
        const stubCallback = () => {};

        callbacks.compareCallback = callbacks.compareCallback || undefined;
        callbacks.visitingCallback = callbacks.visitingCallback || stubCallback;

        return callbacks;
    }

    sort() {
        throw new Error('sort method must be implemented');
    }
}