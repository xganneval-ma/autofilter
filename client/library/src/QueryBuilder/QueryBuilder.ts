import And from "Expressions/And";
import Or from "Expressions/Or";

const isExpression = (value: Criterion): value is Expression => {
  return ["And", "Or", "Not"].includes(value.type);
};

const isExpressionLink = (value: Criterion): value is ExpressionLink => {
  return ["And", "Or"].includes(value.type);
};

const isOperator = (value: Criterion): value is Operator => {
  const operatorType = ["Eq", "Lt", "Lte", "Gt", "Gte", "Like"];
  return operatorType.includes(value.type);
};

const stringifyOperator = (operator: Operator) => {
  return `${operator.type}(${operator.field},'${operator.value}')`;
};

const stringifyExpression = (expression: Expression): string => {
  if (expression.type === "Not") {
    return `${expression.type}(${stringifyOperator(expression.operator)})`;
  }
  return `${expression.type}(${expression.children
    .map((criterion) => stringify(criterion))
    .join(",")})`;
};

const stringify = (criterion: Criterion) => {
  if (isExpression(criterion)) {
    return stringifyExpression(criterion);
  }

  return stringifyOperator(criterion);
};

class QueryBuilder {
  private query?: Operator | Expression;

  filter(criterion: Criterion) {
    if (this.query) {
      throw new Error(
        "Query not empty, use and() or or() to add the criterion"
      );
    }

    this.query = criterion;
    return this;
  }

  and(criterion: Criterion) {
    if (!this.query) {
      throw new Error(
        "Query is empty, you must call filter() once before adding criterion"
      );
    }

    if (
      isExpressionLink(this.query) &&
      isExpressionLink(criterion) &&
      criterion.type === this.query.type
    ) {
      // Same expression, let's merge the children
      this.query.children = [...this.query.children, ...criterion.children];
      return this;
    }

    this.query = And(this.query, criterion);

    return this;
  }

  or(criterion: Criterion) {
    if (!this.query) {
      throw new Error(
        "Query is empty, you must call filter() once before adding criterion"
      );
    }

    if (
      isExpressionLink(this.query) &&
      isExpressionLink(criterion) &&
      criterion.type === this.query.type
    ) {
      // Same expression, let's merge the children
      this.query.children = [...this.query.children, ...criterion.children];
      return this;
    }

    this.query = Or(this.query, criterion);

    return this;
  }

  get() {
    if (this.query) {
      console.log(this.query);
      return stringify(this.query);
    }
    return "";
  }
}

export default QueryBuilder;
