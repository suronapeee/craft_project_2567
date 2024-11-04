// Car.js
import React, { useState } from 'react';

const Header = () => { //new
  return (
    <>
      <h1 style={{backgroundColor: "lightblue"}}>Hello Style!</h1>
      <p>Add a little style!</p>
    </>
  );
}

function Car(props) {
  return <li >I am a { props.brand }</li>;
}
function Garage() {
  const cars = ['volvo']; // Empty array of cars
  let message; // Variable to hold the message

  // Use if statement to determine the message based on cars array length
  if (cars.length > 0) {
    message = <h2>You have {cars.length} cars in your garage.</h2>;
  } else {
    message = <h2>No cars in the garage.</h2>;
  }

  return (
    <>
      {message} {/* Render the message */}
      <ul>
        {cars.map((car) => (
          <Car key={car.id} brand={car.brand} />
        ))}
      </ul>
    </>
  );
}
export default Car;
export {Garage, Header}; //new


