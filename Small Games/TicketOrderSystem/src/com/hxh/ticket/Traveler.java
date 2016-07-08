package com.hxh.ticket;

public class Traveler {
	String name;
	boolean sex;
	Identifier id;
	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}
	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	/**
	 * @return the id
	 */
	public Identifier getId() {
		return id;
	}
	/**
	 * @param id the id to set
	 */
	public void setId(Identifier id) {
		this.id = id;
	}
	
}
