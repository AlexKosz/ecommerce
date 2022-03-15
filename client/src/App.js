import React from 'react';
import './App.css';
import { Router } from "@reach/router";
// import SignIn from './components/SignIn';
import Store from './components/Store';
import ProductPage from './components/ProductPage';
import Navbar from './components/Navbar';
import SignIn from './components/SignIn';


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
        <SignIn path="/sign" urls={urls}/>
        <ProductPage path="/product/:productId" urls={urls}/>
        {/* <SignIn path="/signIn" /> */}
      </Router>


    </div>
  );
}

export default App;
