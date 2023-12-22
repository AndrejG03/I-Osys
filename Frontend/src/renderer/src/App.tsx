import './index.css'
import ncrLogo from './assets/ncrLogo.svg'
import { FiInfo, FiChevronLeft, FiChevronRight, FiCopy } from 'react-icons/fi'

function App(): JSX.Element {
  return (
    <main className="h-screen w-full flex flex-col items-center justify-center gap-8 relative">
      <img src={ncrLogo} alt="NCR VOYIX" className="absolute bottom-6 right-6 w-64" />
      <div className="flex items-center justify-center gap-4">
        <FiInfo className="text-4xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
        <p className="bg-gray-200 py-2 px-3 rounded-md border border-offBlack">DEPT</p>
      </div>
      <div className="flex flex-col items-center gap-2">
        <p className="text-xl">Config item</p>
        <input
          type="text"
          placeholder="Enter in format XX XXXX US"
          className="w-96 border h-10 border-offBlack rounded-md px-3 hover:border-ncrAccent outline-none focus:border-ncrAccent focus-within:shadow-md"
        />
      </div>
      <div className="flex flex-col items-center gap-2">
        <p className="text-xl">Device</p>
        <div className="flex items-center justify-center">
          <FiChevronLeft className="text-4xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
          <input
            type="text"
            placeholder="Search for needed device"
            className="w-96 border h-10 border-offBlack rounded-md px-3 hover:border-ncrAccent outline-none focus:border-ncrAccent focus-within:shadow-md"
          />
          <FiChevronRight className="text-4xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
        </div>
      </div>
      <div className="flex flex-col items-center gap-2">
        <p className="text-xl">Issue</p>
        <div className="flex items-center justify-center">
          <FiChevronLeft className="text-4xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
          <input
            type="text"
            placeholder="Search for issue with selected device"
            className="w-96 border h-10 border-offBlack rounded-md px-3 hover:border-ncrAccent outline-none focus:border-ncrAccent focus-within:shadow-md"
          />
          <FiChevronRight className="text-4xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
        </div>
      </div>
      <button className="px-6 py-3 rounded-full bg-offBlack text-white outline-none border-none hover:bg-ncrAccent hover:shadow-md active:scale-95 transition">
        Give Log
      </button>
      <div className="flex items-center justify-center gap-3">
        <input
          type="text"
          placeholder="First Log"
          className="w-96 border h-10 border-offBlack rounded-md px-3"
          disabled
        />
        <FiCopy className="text-3xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
      </div>
      <div className="flex items-center justify-center gap-3">
        <input
          type="text"
          placeholder="Troubleshoot Log"
          className="w-96 border h-10 border-offBlack rounded-md px-3"
          disabled
        />
        <FiCopy className="text-3xl transition hover:text-ncrAccent hover:scale-105 cursor-pointer active:scale-95" />
      </div>
    </main>
  )
}

export default App
