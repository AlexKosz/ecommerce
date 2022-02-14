import React from 'react';
import './styles/Nav.css';

const Navbar = (props) => {


    return (
        <div className='wrapper'>
            <h2>Logo Goes Here</h2>
            <div className='search'>
                <img src='searchicon.png' alt=""/>
                <input type="text" />
            </div>
            <div className='right'>
                <a><h3>Home</h3></a>
                <a><h3>Account</h3></a>

                <div className='cart'>
                    <h4>0</h4>
                    <h4>C</h4>
                </div>
            </div>




        </div>




    );
}

export default Navbar;