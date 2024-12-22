import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar';
import Dropdown from './components/Dropdown';

function App() {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/jobs/')
            .then(response => {
                console.log(response.data);
                setJobs(response.data);
                setLoading(false);
            })
            .catch(error => console.error("Error fetching job data:", error));
    }, []);

    if (loading) {
        return <p>Loading jobs...</p>;
    }    
  
    return (
        <div className="bg-gray-100 min-h-screen">
            <Navbar />
          {/* Header Section */}
          <header className="bg-white p-4 mt-5 mx-48 rounded-2xl">
            <div className="bg-slate-100 max-w-5xl mx-auto flex flex-col gap-4 p-3 rounded-2xl">
                <div className="relative w-full">
                    <input
                        type="text"
                        placeholder="Search by job title"
                        className="border border-gray-300 rounded-full px-4 py-2 w-full"
                    />
                    <button
                        type="button"
                        className="absolute right-1 top-1 bottom-1 px-2 bg-blue-600 text-white rounded-full hover:bg-blue-600 focus:ring-2 focus:ring-blue-300"
                        >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            strokeWidth="2"
                            stroke="currentColor"
                            className="w-5 h-5"
                        >
                            <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M21 21l-4.35-4.35m2.35-5.15a7 7 0 11-14 0 7 7 0 0114 0z"
                            />
                        </svg>
                    </button>
                </div>
              <div className="flex flex-wrap gap-2">
                <Dropdown
                    label="Job Type"
                    options={["Full-Time", "Part-Time", "Contract"]}
                />
                <Dropdown
                    label="Workplace"
                    options={["On-site", "Remote", "Hybrid"]}
                />
                <Dropdown
                    label="Country or Timezone"
                    options={["USA", "India", "Europe", "Asia"]}
                />
                <Dropdown
                    label="Seniority"
                    options={["Junior", "Mid-Level", "Senior", "Lead"]}
                />
                <Dropdown
                    label="Pay"
                    options={["15-20 USD/hour", "20-30 USD/hour", "Above 30 USD/hour"]}
                />
                <Dropdown
                    label="Travel"
                    options={["No Travel", "Occasional", "Frequent"]}
                />
              </div>
            </div>
          </header>
          <div className='flex justify-end mr-48 mt-6'>
            <Dropdown
                label="Most Recent"
                options={["Most Recent", "Pay (high to low)", "Pay (low to high)"]}
            />
          </div>
          {/* Job Cards Section */}
          <main className="max-w-5xl mx-auto p-4">
            {jobs.map((job) => (
                <a href={job.details_url}>
                    <div
                        key={job.id}
                        className="flex items-center bg-white p-4 shadow rounded-lg mb-4"
                    >
                        <div className="flex-grow">
                            <p className="text-sm text-gray-400">{job.posted_date}</p>
                        <h3 className="font-semibold text-lg">{job.title}</h3>
                        <p className="text-gray-500">{job.company}</p>
                        </div>
                        <div className="flex flex-col justify-end">
                            <p className="text-sm text-right font-medium text-gray-700">{job.salary} USD/year</p>
                            <div className="flex gap-2">
                                <p className="text-sm text-gray-400">{job.location}</p>
                                <p className="text-sm text-gray-400">{job.employment_type}</p>
                            </div>
                        </div>
                    </div>
              </a>
            ))}
          </main>
        </div>
      );
}

export default App;
