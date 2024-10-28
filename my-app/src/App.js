import './App.css';
import Car, {Garage, Header} from './Car'; //new  
import MyForm from './My_form'; 
import { Routes, Route } from 'react-router-dom';
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Blogs from "./pages/Blogs";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";
import FavoriteColor from "./Hook.js";

function App() {
  return (
    <div className="App">
      <h1>Welcome to my Car App!</h1>
      <Routes> 
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="blogs" element={<Blogs />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
      <Header /> {/*new*/} 
      <Garage /> 
      <MyForm />
      <FavoriteColor/>
    </div>
  );
}

export default App;
