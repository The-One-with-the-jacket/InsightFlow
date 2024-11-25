import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const GroupPage = () => {
    return (
        <div id="groups" className="page active">
            <Navbar />
            <div id="container">
                <h1>Group Page</h1>
                <p>This is the group page.</p>
            </div>
            <Footer />
        </div>
    );
};

export default GroupPage;
