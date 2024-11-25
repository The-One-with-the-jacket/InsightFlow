import React from 'react';

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/profile">Profile</a></li>
                <li><a href="/groups">Groups</a></li>
                <li><a href="/chat">Chat</a></li>
            </ul>
        </nav>
    );
};

export default Navbar;
