import React, { Component } from "react";

export default class Base extends Component {
    constructor(props) {
        super(props);
    }


render() {
    return (
        <html>
<body>
    <div class="sidenav">
        <a href="/multimario">Home</a>
        <a href="/upcomingraces">Upcoming Races</a>
        <a href="/multimario">Community Events</a>
        <a href="/multimario">Past Races Archive</a>
        <a href="/multimario/glossary">Glossary</a>
        <a href="/login">Login</a>
    </div>
</body>
</html>
    )
}
}