import React, { Component } from "react";
import { render } from "react-dom";
import Base from './Base';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <Base />
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);