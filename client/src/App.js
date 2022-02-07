import React from 'react';
import './App.css';
import { Router } from "@reach/router";
// import SignIn from './components/SignIn';
import Store from './components/Store';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Router>
        <Store path="/" />
        {/* <SignIn path="/signIn" /> */}
      </Router>


    </div>
  );
}

export default App;
