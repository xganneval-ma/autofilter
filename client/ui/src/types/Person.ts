interface Contact {
    id: number;
    type: string;
    value: string;
    is_public: boolean;
    owner_id: number;
}

export interface Person {
    id: number;
    name: string;
    first_name: string;
    birthdate: string;
    gender: {
        id: number;
        value: 'Female' | 'Male';
    };
    email: Contact;
    cellphones: Contact[];
}
