import React from "react";
import Header from "../components/header";
import Footer from "../components/footer";

function Inicio() {
    return (
    <>
    <Header/>
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
            <div className="course-card">
                <img src="https://placehold.co/300x180/E0E0E0/333333?text=Curso+1" alt="Curso de Programación" />
                <h3>Programación Web con Python</h3>
                <p>Aprende a crear aplicaciones web robustas y escalables.</p>
                <div className="course-meta">
                    <span>★ 4.7</span>
                    <span>(1200 alumnos)</span>
                </div>
                <button className="btn btn-card">Ver Curso</button>
            </div>
        </div>
    </section>

    <Footer/>
        </>
    );
}

export default Inicio;