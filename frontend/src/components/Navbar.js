import React from "react";

export default function Navbar() {
  return (
    <nav className="bg-white px-6 py-3">
      <div className="flex items-center gap-32">
        {/* Logo */}
        <div className="flex items-center">
          <img
            src="https://via.placeholder.com/40"
            alt="Logo"
            className="w-8 h-8 rounded-full mr-2"
          />
        </div>

        {/* Links */}
        <div className="max-w-7xl flex items-center gap-64 space-x-6">
          <span className="text-lg font-bold">JobListing/jobs</span>
            {/* Action Buttons */}
            <div className="flex items-center space-x-4">
                <a href="#" className="text-gray-600 hover:text-black">
                    For job seekers
                </a>
                <a href="#" className="text-gray-600 hover:text-black">
                    For employers
                </a>
                <a href="#" className="text-gray-600 hover:text-black">
                    Pricing
                </a>
                <a
                    href="#"
                    className="text-blue-500 hover:text-blue-600 font-medium flex items-center"
                >
                    <span className="mr-1 text-xl">+</span> Post a job
                </a>
                <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
                    Sign up
                </button>
                <button className="border border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-100">
                    Log in
                </button>
            </div>
        </div>
      </div>
    </nav>
  );
}
