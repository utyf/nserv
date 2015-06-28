/* shortcuts */
var el = React.createElement;

/* helpers */
var MINUTE = 60 * 1000,
    HOUR = 60 * MINUTE,
    DAY = 24 * HOUR;

/**
 * Returns string representation of time
 * passed from particular moment
 */
function timePassed(current, past) {
    var passed = current - past;
    if (passed < MINUTE) {
        return '< 1 min';
    }

    if (passed < HOUR) {
        return String(Math.floor(passed / MINUTE)) + ' min';
    }

    if (passed < DAY) {
        return String(Math.floor(passed / HOUR)) + ' hrs';
    }

    return String(Math.floor(passed / DAY)) + ' days';

}

/* to avoid precompilation, dom structure is described without JSX */
var Notification = React.createClass({
    render: function() {
        return (
            el(
                'div', 
                { "className": "alert alert-" + this.props.level }, 
                [
                    el('strong', null, timePassed(
                        this.props.currentTime, 
                        this.props.timestamp
                    ) + ' ago'),
                    ' ',
                    this.props.text
                ]
            )
        );
    }
});

/**
 * Root element (notification list)
 */
var Root = React.createClass({
    render: function() {
        var currentTime = this.props.currentTime,
            notifications;

        notifications = this.props.notifications.map(function(item) {
            /* pass currentTime to children */
            item.currentTime = currentTime;
            return el(Notification, item);
        });
        return el('div', null, notifications);
    }
});
