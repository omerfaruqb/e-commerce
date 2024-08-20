import React from "react";
import { Link } from "react-router-dom";

const Button = ({ buttonName, buttonUrl }) => {
  return (
    <div>
      <Link to={buttonUrl}>
        <p className="m-1.5 pt-1.5 pb-1.5 px-2 bg-orange-500 text-white hover:bg-orange-400 hover:border-white rounded-2xl hover:cursor-pointer">
          {buttonName}
        </p>
      </Link>
    </div>
  );
};

export default Button;
