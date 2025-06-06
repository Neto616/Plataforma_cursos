// Importación de React y hooks necesarios
import React, { useEffect, useState } from "react";

// Importación de componentes reutilizables (Header, Footer y tarjetas de curso)
import Header from "../components/header";
import Footer from "../components/footer";
import CourseCard from "../components/cursoCard";

function Inicio() {
    // Estado para almacenar los cursos obtenidos del backend
    const [courses, setCourses] = useState([]);

    // Función asíncrona que obtiene la lista de cursos desde el backend
    const getCourses = async () => {
        try {
            const peticion = await fetch("http://localhost:8000/obtener_cursos", {
                method: "GET",
                headers: { "Content-Type": "application/json" }
            });

            const resultado = await peticion.json(); // Parsear la respuesta JSON
            console.log(resultado); // Mostrar en consola para depuración

            // Si no se obtuvo correctamente, dejar la lista vacía
            if (!resultado.estatus) return setCourses([]);

            // Si todo está bien, se actualiza el estado con los cursos
            setCourses(resultado.result.cursos);
        } catch (error) {
            // Si ocurre algún error en la petición
            console.error("Ha ocurrido un error al obtener los cursos: ", error);
            setCourses([]); // Dejar cursos vacío si hay fallo
        }
    };

    // Hook useEffect para llamar a getCourses una vez cuando se monta el componente
    useEffect(() => {
        getCourses();
    }, []);

    // Renderizado del componente
    return (
        <>
            {/* Encabezado */}
            <Header />

            {/* Sección de bienvenida o presentación */}
            <section className="hero-section">
                <div className="hero-content">
                    <h1>Aprende nuevas habilidades en línea</h1>
                    <p>Conviértete en un experto con los mejores cursos impartidos por profesionales.</p>
                    {/* Aquí puedes activar el botón de acción si deseas */}
                    {/* <a href="#" className="btn btn-hero">Explorar Cursos</a> */}
                </div>
            </section>

            {/* Sección de cursos disponibles */}
            <section className="courses-section">
                <h2>Cursos Populares</h2>

                {/* Grid para mostrar CourseCards, si hay cursos */}
                <div className="course-grid">
                    {courses.length ? (
                        // Si hay cursos, se renderiza una tarjeta para cada curso
                        courses.map((e, i) => (
                            <CourseCard 
                                key={i}
                                titulo={e.titulo}
                                imgName={e.portada}
                                id={e.id}
                            />
                        ))
                    ) : (
                        // Si no hay cursos aún
                        <h1>
                            Todavía no tenemos cursos, pero espéralos junto con nosotros
                            para poder certificarte con nosotros.
                        </h1>
                    )}
                </div>
            </section>

            {/* Pie de página */}
            <Footer />
        </>
    );
}

// Exportar el componente para ser usado en otras rutas
export default Inicio;
