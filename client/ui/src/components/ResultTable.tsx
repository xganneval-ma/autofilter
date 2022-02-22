import {Person} from './../types/Person'

interface ResultTableProps {
    persons: Person[] | [];
}

function ResultTable({persons}: ResultTableProps) {
    if (!persons) return null;

    return(
        <table className="table">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>First name</th>
                    <th>Email</th>
                    <th>Birthdate</th>
                    <th>Gender</th>
                </tr>
            </thead>
            <tbody>
                {!persons.length && (
                    <tr>
                        <td>
                            Aucun résultat correspondant à vos critères de sélection
                        </td>
                    </tr>
                )}

                {persons.map((person, index) => {
                    const {id, name, first_name, email, birthdate, gender} = person;

                    return(
                        <tr key={index}>
                            <td>{id ?? id}</td>
                            <td>{name && name}</td>
                            <td>{first_name && first_name}</td>
                            <td>{email?.value && email.value.toLowerCase()}</td>
                            <td>{birthdate && birthdate}</td>
                            <td>{gender?.value && gender.value}</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    )
}

export default ResultTable;
