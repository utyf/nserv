/* state of application */
var state = {
    notifications: [],
    currentTime: Date.now()
};

/**
 * Renders DOM for the page
 *
 * Takes whole state as argument
 */
function renderDOM(state) {
    React.render(
        el(Root, state),
        document.getElementById('main')
    );
}

/**
 * Takes pure function that takes old state and returns new one
 * Return function, that updates the state and renders DOM
 */
function wrapAction(pureAction) {
    return function() {
        var args = Array.prototype.slice.call(arguments),
            newState;

        /* state of application */
        state = pureAction(state, args);
        renderDOM(state);
    }
}

/**
 * Adds new notification to the state
 */
function wsMessageAction(state, params) {
    var notification = JSON.parse(params[0].data);
    notification.timestamp = Date.now();

    state.notifications.push(notification);
    /* update current time as well */
    return currentTimeAction(state);
}

/**
 * Sets current time on the state
 */
function currentTimeAction(state) {
    state.currentTime = Date.now();
    return state;
}


function init() {
    var ws = new WebSocket('ws://localhost:8080/notifications');
    ws.onmessage = wrapAction(wsMessageAction);

    /* Update UI every 10 sec */
    setInterval(wrapAction(currentTimeAction), 10000);
}

init();
