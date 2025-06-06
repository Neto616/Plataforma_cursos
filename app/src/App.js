// Importación de React para poder usar JSX
import React from 'react';

// Importación de componentes necesarios de React Router para la navegación
import { Routes, Route, BrowserRouter } from "react-router-dom";

// Importación de las vistas que se usarán como páginas
import Login from './views/login';
import "./styles/global.css"; // Importación de estilos globales
import SignUp from './views/signup';
import Inicio from './views/inicio';
import CursoCaps from './views/cursoCaps';

// Componente principal de la aplicación
function App() {

    return (
        // BrowserRouter permite el manejo del enrutamiento con historial del navegador
        <BrowserRouter>
            <div className='App'>
                {/* Routes contiene todos los elementos Route que definen las rutas de la app */}
                <Routes>
                    {/* Ruta principal que muestra la vista de inicio */}
                    <Route path="/" element={<Inicio />} />

                    {/* Ruta para mostrar los capítulos de un curso específico */}
                    <Route path="/capitulos/:curso" element={<CursoCaps />} />

                    {/* Ruta para la vista de inicio de sesión */}
                    <Route path="/iniciar-sesion" element={<Login />} />

                    {/* Ruta para la vista de registro */}
                    <Route path="/sign-up" element={<SignUp />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

// Exportación del componente App para que pueda ser usado en otros archivos
export default App;
