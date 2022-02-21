import And from "Expressions/And";
import Or from "Expressions/Or";
import Eq from "Operators/Eq";
import QueryBuilder from "./QueryBuilder";

describe("QueryBuilder", () => {
  it("test", () => {
    const Q = new QueryBuilder();

    // Simpliest
    // console.log(Q.filter(Eq("A", "1")).get());

    // And only
    // console.log(Q.filter(Eq("A", "1")).and(Eq("B", "2")).get());
    // console.log(
    //   Q.filter(Eq("A", "1")).and(Eq("B", "2")).and(Eq("C", "3")).get()
    // );
    // console.log(Q.filter(And(Eq("A", "1"), Eq("B", "2"))).get());
    // console.log(
    //   Q.filter(And(Eq("A", "1"), Eq("B", "2")))
    //     .and(Eq("C", "3"))
    //     .get()
    // );

    // Or only
    // console.log(Q.filter(Eq("A", "1")).or(Eq("B", "2")).get());
    // console.log(Q.filter(Or(Eq("A", "1"), Eq("B", "2"))).get());
    // console.log(
    //   Q.filter(Or(Eq("A", "1"), Eq("B", "2")))
    //     .or(Eq("C", "3"))
    //     .get()
    // );

    // Mix and / or
    // console.log(Q.filter(Eq("A", "1")).and(Eq("B", "2")).or(Eq("A", "2")).get());
    // console.log(Q.filter(Eq("A", "1")).or(Eq("A", "2")).and(Eq("B", "1")).get());
    console.log(Q.filter(Eq('A', '1')).and(Eq('B', '1')).or(Eq('A', '2')).and(Eq('C', '1')).get());
  });
});
