import React from "react";

// Componente Footer: muestra el pie de página de la plataforma.
// Incluye texto de derechos reservados y enlaces (a modo de ejemplo) a páginas de privacidad, términos y contacto.

function Footer() {
    return (
        <footer className="main-footer">
            <div className="footer-content">
                {/* Texto de derechos de autor */}
                <p>&copy; 2024 Plataforma de Cursos. Todos los derechos reservados.</p>

                {/* Enlaces informativos del footer */}
                <div className="footer-links">
                    <a href="#">Privacidad</a>
                    <a href="#">Términos</a>
                    <a href="#">Contacto</a>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
