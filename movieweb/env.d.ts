/// <reference types="vite/client" />


declare global{
    interface Response<T = {}>{
        code:number;
        msg:string;
        data:T;
    }
    interface ImportMetaEnv {
        VITE_APP_URL: string;
        VITE_ENV : string;
        VITE_APP_MODE :string;
      }

}
export {};