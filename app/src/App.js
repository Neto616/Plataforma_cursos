import React from 'react';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Login from './views/login';
import "./styles/global.css"

function App() {

    return (
        <BrowserRouter>
         <div className='App'>
            <Routes>
                <Route path="/" element={<Login/>}></Route>
            </Routes>
         </div>
        </BrowserRouter>
    );
}

export default App;