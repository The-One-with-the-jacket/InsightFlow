import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ProfilePage from './pages/ProfilePage';
import GroupPage from './pages/GroupPage';
import ChatPage from './pages/ChatPage';

const App = () => {
    return (
        <Router>
            <div>
                <Switch>
                    <Route exact path="/" component={HomePage} />
                    <Route path="/profile" component={ProfilePage} />
                    <Route path="/groups" component={GroupPage} />
                    <Route path="/chat" component={ChatPage} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;
