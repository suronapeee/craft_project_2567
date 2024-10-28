import React, { useState } from "react";

function FavoriteColor() {
  // Initialize state by calling useState function, which returns two values:
  // (1) current state and (2) A function that updates the state.
  const [color, setColor] = useState("red");
  const [car, setCar] = useState({ // use one state to keep track of object
    brand: "Ford",
    model: "Mustang",
    year: "1964",
    color: "red"
  });
  const updateColor = () => {
    setCar(previousState => { // This function receives the previous value.
      //return an object, spreading the previousState and overwriting only the color.
      return { ...previousState, color: "blue" , model: "Falcon"}
    });
  }
  // example of using state
  return (
  <>
    <h1>My favorite color is {color}!</h1>
    <p>
      It is a {car.color} {car.model} from {car.year}.
    </p>
    <button
      type="button"
      onClick={() => setColor("blue")} 
    >Blue</button> {/* onClick={updateColor} for update object state */}
  </>
  );
}

export default FavoriteColor;
