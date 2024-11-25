import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const ProfilePage = () => {
    return (
        <div id="profile" className="page active">
            <Navbar />
            <div id="container">
                <h1>Profile Page</h1>
                <p>This is the profile page.</p>
            </div>
            <Footer />
        </div>
    );
};

export default ProfilePage;
