import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const ChatPage = () => {
    return (
        <div id="chat" className="page active">
            <Navbar />
            <div id="container">
                <h1>Chat Page</h1>
                <p>This is the chat page.</p>
            </div>
            <Footer />
        </div>
    );
};

export default ChatPage;
