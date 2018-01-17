// EventDispatcher assigns e

var Event = function (sender) {
    this._sender = sender;
    this._listeners = [];
}

// Check if writing Event.prototype.attach is the same as the below notation.
Event.prototype = {

    attach: function(listener) {
        this._listeners.push(listener);
    },

    notify: function(args) {
        // This may be an issue, although it shouldn't be.
        for (index = 0; index < this._listeners.length; index += 1) {
            this._listeners[index](this._sender, args);
        }
    }
};