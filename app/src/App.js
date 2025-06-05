import React from 'react';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Login from './views/login';
import "./styles/global.css"
import SignUp from './views/signup';

function App() {

    return (
        <BrowserRouter>
         <div className='App'>
            <Routes>
                <Route path="/" element={<Login/>}></Route>
                <Route path="/sign-up" element={<SignUp/>}></Route>
            </Routes>
         </div>
        </BrowserRouter>
    );
}

export default App;