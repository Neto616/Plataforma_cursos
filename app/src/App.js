import React from 'react';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Login from './views/login';
import "./styles/global.css"
import SignUp from './views/signup';
import Inicio from './views/inicio';
import CursoCaps from './views/cursoCaps';

function App() {

    return (
        <BrowserRouter>
         <div className='App'>
            <Routes>
                <Route path="/" element={<Inicio/>}></Route>
                <Route path="/capitulos/:curso" element={<CursoCaps/>}></Route>
                <Route path="/iniciar-sesion" element={<Login/>}></Route>
                <Route path="/sign-up" element={<SignUp/>}></Route>
            </Routes>
         </div>
        </BrowserRouter>
    );
}

export default App;