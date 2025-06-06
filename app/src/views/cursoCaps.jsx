// Importación de React y hooks necesarios
import React, { useEffect, useState } from "react";

// Estilos globales para el componente
import "../styles/global.css";

// Hook para obtener la URL actual
import { useLocation } from "react-router-dom";

function CursoCaps() {
  // Hook para acceder a la ruta actual (por ejemplo: /curso/1)
  const location = useLocation();

  // Estado que guarda todos los capítulos del curso
  const [chapters, setChapters] = useState([]);

  // Estado para la URL del video actualmente seleccionado
  const [videoUrl, setVideoUrl] = useState("");

  // Estado para abrir o cerrar módulos (como un acordeón)
  const [modulosAbiertos, setModulosAbiertos] = useState({});

  // Función que obtiene los capítulos desde el backend
  const getChapters = async () => {
    try {
      // Hace una petición GET al backend usando la ruta actual
      const response = await fetch("http://localhost:8000" + location.pathname, {
        method: "GET",
        headers: { "Content-Type": "application/json" }
      });

      const data = await response.json(); // Parseo de la respuesta JSON

      setChapters(data || []); // Guardar capítulos recibidos

      // Si hay capítulos, se carga el primer video automáticamente
      if (data.length > 0) {
        setVideoUrl(embedUrl(data[0].url));
      }
    } catch (error) {
      console.error("Error al obtener los capítulos:", error);
    }
  };

  // useEffect se ejecuta cuando el componente se monta o cambia la URL
  useEffect(() => {
    getChapters();
  }, [location.pathname]);

  // Función que alterna si un módulo está abierto o cerrado
  const toggleLessons = (id) => {
    setModulosAbiertos((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  // Carga un nuevo video al hacer clic en una lección
  const loadYoutubeVideo = (url) => {
    setVideoUrl(embedUrl(url));
  };

  // Convierte una URL de YouTube a una URL embebida (embed)
  const embedUrl = (youtubeUrl) => {
    // Extrae el ID del video con una expresión regular
    const match = youtubeUrl.match(/(?:\/|v=|be\/|embed\/)([a-zA-Z0-9_-]{11})/);
    return match ? `https://www.youtube.com/embed/${match[1]}` : "";
  };

  // Renderizado del componente
  return (
    <section className="course-player-page">
      <div className="course-player-container">

        {/* Sección del video principal */}
        <div className="video-player">
          <div className="video-header">
            <h1>Curso - Capítulo {chapters[0]?.capitulo}</h1>
          </div>

          {/* Video de YouTube embebido */}
          <div className="youtube-player-wrapper">
            <iframe
              width="100%"
              height="100%"
              src={videoUrl}
              title="YouTube video player"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerPolicy="strict-origin-when-cross-origin"
              allowFullScreen
            ></iframe>
          </div>

          {/* Descripción del curso */}
          <div className="course-description-area">
            <h2>Descripción General</h2>
            <p>{chapters[0]?.descripcion}</p>
            <p className="course-rating">★ 4.7 (1200 alumnos)</p>
          </div>
        </div>

        {/* Sección del listado de capítulos */}
        <div className="chapter-list-container">
          <h2>Contenido del Curso</h2>
          <div className="modules-list">

            {/* Módulo con botón para abrir/cerrar lista de lecciones */}
            <div className="module-item">
              <div className="module-title" onClick={() => toggleLessons("mod1")}>
                <h3>Capítulos</h3>
                <span className="toggle-icon">{modulosAbiertos["mod1"] ? "−" : "+"}</span>
              </div>

              {/* Lista de capítulos, si el módulo está abierto */}
              {modulosAbiertos["mod1"] && (
                <ul className="lesson-list">
                  {chapters.map((chapter, index) => (
                    <li className="lesson-item" key={index}>
                      <a href="#" onClick={() => loadYoutubeVideo(chapter.url)}>
                        <span className="lesson-number">{chapter.capitulo}</span> {chapter.descripcion}
                        <span className="lesson-duration">{chapter.duracion} min</span>
                      </a>
                    </li>
                  ))}
                </ul>
              )}
            </div>

          </div>
        </div>
      </div>
    </section>
  );
}

// Exportación del componente para usarlo en rutas
export default CursoCaps;
