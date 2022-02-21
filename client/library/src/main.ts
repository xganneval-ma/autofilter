import QueryBuilder from "./QueryBuilder/QueryBuilder";

const createQueryBuilder = () => {
  return new QueryBuilder();
};

export * from "Operators";
export * from "Expressions";
export default createQueryBuilder;
