import React from "react";
import { Link, useNavigate } from "react-router-dom";

function Header(){
    return (
    <header className="main-header">
        <div className="header-content">
            <div className="logo">
                <a href="#">PlataformaCursos</a>
            </div>
            <nav className="main-nav">
                <ul>
                    <li><a href="#">Categorías</a></li>
                    <li><a href="#">Mis Cursos</a></li>
                    <li><Link to="/iniciar-sesion" className="btn btn-secondary">Iniciar Sesión</Link></li>
                    <li><Link to="/sign-up" className="btn btn-primary">Registrarse</Link></li>
                </ul>
            </nav>
        </div>
    </header>
    );
}

export default Header;