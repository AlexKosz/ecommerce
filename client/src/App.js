import React from 'react';
import './App.css';
import { Router } from "@reach/router";
// import SignIn from './components/SignIn';
import Store from './components/Store';
import Navbar from './components/Navbar';


const baseURL = 'http://localhost:8000'

const urls = {
  'baseURL':baseURL,
  'apiURL':`${baseURL}/api`
}



function App() {
  return (
    <div className="App">
      <Navbar />
      <Router>
        <Store path="/" urls={urls}/>
        {/* <SignIn path="/signIn" /> */}
      </Router>


    </div>
  );
}

export default App;
