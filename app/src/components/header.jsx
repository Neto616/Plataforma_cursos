import React from "react";
import { Link } from "react-router-dom"; // Link se usa para navegación interna sin recargar la página

// Componente Header: muestra la cabecera principal de la plataforma con logo y navegación
function Header() {
    return (
        <header className="main-header"> {/* Encabezado principal del sitio */}
            <div className="header-content"> {/* Contenedor del contenido del header */}
                
                {/* Logo de la plataforma */}
                <div className="logo">
                    {/* Actualmente es un <a href="#">, lo cual recarga la página.
                        Recomendación: usar <Link to="/"> para SPA */}
                    <a href="#">PlataformaCursos</a>
                </div>

                {/* Navegación principal */}
                <nav className="main-nav">
                    <ul>
                        {/* Enlaces de navegación. Se podrían convertir a <Link> si llevan a rutas internas */}
                        <li><a href="#">Categorías</a></li>
                        <li><a href="#">Mis Cursos</a></li>

                        {/* Botón para ir a la vista de inicio de sesión */}
                        <li>
                            <Link to="/iniciar-sesion" className="btn btn-secondary">
                                Iniciar Sesión
                            </Link>
                        </li>

                        {/* Botón para ir a la vista de registro */}
                        <li>
                            <Link to="/sign-up" className="btn btn-primary">
                                Registrarse
                            </Link>
                        </li>
                    </ul>
                </nav>

            </div>
        </header>
    );
}

export default Header;
