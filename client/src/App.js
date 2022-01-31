import React from 'react';
import './App.css';
import { Router } from "@reach/router";
// import SignIn from './components/SignIn';
import Store from './components/Store';

function App() {
  return (
    <div className="App">
      <Router>
        <Store path="/" />
        {/* <SignIn path="/signIn" /> */}
      </Router>


    </div>
  );
}

export default App;
