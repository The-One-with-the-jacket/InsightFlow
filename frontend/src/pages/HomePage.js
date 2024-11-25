import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const HomePage = () => {
    return (
        <div id="home" className="page active">
            <Navbar />
            <div id="container">
                <h1>Welcome to The Insight</h1>
                <p>Your go-to platform for insightful group interactions and more!</p>
            </div>
            <Footer />
        </div>
    );
};

export default HomePage;
