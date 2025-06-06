import React, { useEffect, useState } from "react";
import Header from "../components/header";
import Footer from "../components/footer";
import CourseCard from "../components/cursoCard";

function Inicio() {
    const [courses, setCourses] = useState([]);

    const getCourses = async () => {
        try {
            const peticion = await fetch("http://localhost:8000/obtener_cursos", {
                method: "GET",
                headers: { "Content-Type": "application/json" }
            })
            const resultado = await peticion.json();
            console.log(resultado)
            if(!resultado.estatus) return setCourses([])
            setCourses(resultado.result.cursos);
        } catch (error) {
            console.error("Ha ocurrido un error al obtener los cursos: ", error);
            setCourses([]);
        }
    }

    useEffect(()=>{
        getCourses();
    }, [])

    return (
        <>
            <Header />
            <section className="hero-section">
                <div className="hero-content">
                    <h1>Aprende nuevas habilidades en línea</h1>
                    <p>Conviértete en un experto con los mejores cursos impartidos por profesionales.</p>
                    {/* <a href="#" className="btn btn-hero">Explorar Cursos</a> */}
                </div>
            </section>

    <section className="courses-section">
        <h2>Cursos Populares</h2>
        <div className="course-grid">
            {courses.length ? (courses.map((e, i) => <CourseCard key={i} titulo={e.titulo} imgName={e.portada} id={e.id}/> ) ) 
            : (<h1>Todavia no tenemos cursos pero esperalos junto con nosotros
                para poder certificarte con nosotros
            </h1>)}
        </div>
    </section>

            <Footer />
        </>
    );
}

export default Inicio;
